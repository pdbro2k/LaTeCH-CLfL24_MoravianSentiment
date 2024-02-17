def format_boxplot(ax, xlabel, ylabel):
    ax.set_facecolor("white")
    ax.spines['top'].set_color("white")
    ax.spines['right'].set_color("white")

    for tick in ax.xaxis.get_major_ticks():
        tick.label1.set_fontsize(24)
        tick.label1.set_rotation(45)
    for tick in ax.yaxis.get_major_ticks():
        tick.label1.set_fontsize(24)
    ax.set_xlabel(xlabel, fontsize=28)
    ax.set_ylabel(ylabel, fontsize=28)
    ax.legend(prop=dict(size=24))

    ax.set(ylim=(-1, 1))