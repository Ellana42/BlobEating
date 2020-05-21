import matplotlib.pyplot as plt


def avg(list):
    return sum(list) / len(list)


class Display:
    def __init__(self, world):
        self.world = world
        self.food_icon = ' #'
        self.blob_icon = ' 2'
        self.empty_space = '  '

    def display(self):
        w, h = self.world.get_dimensions()

        print('_' * 2 * (w + 1))
        for y in range(h):
            print("|", end='')
            for x in range(w):
                if (x, y) in self.world.food:
                    print(self.food_icon, end='')
                elif (x, y) in self.world.get_blob_positions():
                    print(self.blob_icon, end='')
                else:
                    print(self.empty_space, end='')
            print("|")

        print('-' * (w + 1) * 2)


def plot(stats, chosen_stats=['gratefulness', 'altruism_index', 'altruism_proportion', 'nb_blobs', 'food_left']):
    formatted_stats = {}
    formatted_stats['gratefulness'], formatted_stats['altruism_index'] = format(
        stats)
    formatted_stats['nb_blobs'] = [stat['nb_blobs'] for stat in stats]
    formatted_stats['food_left'] = [stat['food_left'] for stat in stats]
    rounds = range(len(stats))

    fig, axes = plt.subplots(len(chosen_stats), 1, figsize=(20, 8))
    fig.subplots_adjust(hspace=2)
    i = 0
    for stat_name, stat in formatted_stats.items():
        axe = axes[i]
        if type(stat) == dict:
            for name_diff_stat, diff_stat in stat.items():
                axe.plot(rounds, diff_stat, label=name_diff_stat)
            axe.legend()
        else:
            axe.plot(rounds, stat)
        axe.set_xlabel('rounds')
        axe.set_ylabel(stat_name)
        i += 1
    plt.show()


def format(stats):

    # Gratefulness
    max_grate = []
    min_grate = []
    avg_grate = []
    for stat in stats:
        max_grate.append(max(stat['gratefulness']))
        min_grate.append(min(stat['gratefulness']))
        avg_grate.append(avg(stat['gratefulness']))
    gratefulness = {'max_grate': max_grate,
                    'avg_grate': avg_grate, 'min_grate': min_grate}

    # Avg stats on altruism
    max_altruism = []
    min_altruism = []
    avg_altruism = []
    for stat in stats:
        max_altruism.append(max(stat['altruism']))
        min_altruism.append(min(stat['altruism']))
        avg_altruism.append(avg(stat['altruism']))
    altruism_index = {'max_altruism': max_altruism,
                      'avg_altruism': max_altruism,
                      'min_altruism': min_altruism}

    # Quartiles altruism
    first_quartile = []
    half_quartile = []
    third_quartile = []
    for stat in stats:
        first_quartile.append(len(
            [altruism for altruism in stat['altruism'] if altruism < 0.25]) / stat['nb_blobs'] * 100)
        half_quartile.append(len(
            [altruism for altruism in stat['altruism'] if altruism < 0.50]) / stat['nb_blobs'] * 100)
        third_quartile.append(len(
            [altruism for altruism in stat['altruism'] if altruism < 0.75]) / stat['nb_blobs'] * 100)
        altruism_proportion = {
            'first_quartile': first_quartile,
            'half_quartile': half_quartile,
            'third_quartile': third_quartile}

    return gratefulness, altruism_index
