import numpy as np

import evaluate
from transformers import AutoTokenizer, AutoModelForSequenceClassification, TrainingArguments, Trainer

def id2label(dataset):
    return {i: label for i, label in enumerate(dataset.features["label"].names)}

def label2id(dataset):
    return {label: i for i, label in enumerate(dataset.features["label"].names)}

def get_model(base_model, tokenizer, dataset, output_dir):
    # tokenize dataset
    def tokenize_function(examples):
        return tokenizer(examples["text"], padding="max_length", truncation=True)
    dataset = dataset.map(tokenize_function, batched=True)

    # init model
    model = AutoModelForSequenceClassification.from_pretrained(base_model, num_labels=len(label2id(dataset["train"])))

    # init trainer
    def compute_metrics(eval_pred):
        logits, labels = eval_pred
        predictions = np.argmax(logits, axis=-1)
        return evaluate.load("accuracy").compute(predictions=predictions, references=labels)

    training_args = TrainingArguments(output_dir=output_dir + "_trainer", evaluation_strategy="epoch")

    trainer = Trainer(
        model=model, tokenizer=tokenizer,
        args=training_args,
        train_dataset=dataset["train"],
        eval_dataset=dataset["test"],
        compute_metrics=compute_metrics,
    )

    # train
    trainer.train()
    
    # fix labels
    trainer.model.config.id2label = id2label(dataset["train"])
    trainer.model.config.label2id = label2id(dataset["train"])
    
    # store model
    trainer.save_model(output_dir)
    
    return trainer.model