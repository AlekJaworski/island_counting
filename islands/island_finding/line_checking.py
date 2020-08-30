from equivalence_classes.equivalence_class import EquivalenceTable


def remap_colours(colours):
    distinct_colours = set(colours)
    return {key: val + 1 for val, key in enumerate(distinct_colours)}


def check_consecutive_lines(linetop, linebot):
    counter = 0
    bot_last_colour = 0
    top_last_colour = 0
    linebot = ensure_negative_colours(linebot)

    colour_tree = EquivalenceTable.create_from_list([*linetop, *linebot])

    for i, (top_entry, bot_entry) in enumerate(zip(linetop, linebot)):
        counter += count_based_on_four_vertices(bot_entry, top_entry, top_last_colour, bot_last_colour, colour_tree)
        top_last_colour, bot_last_colour = top_entry, bot_entry

    recoloured_bot_line = get_new_colours(colour_tree, linebot)
    return counter, recoloured_bot_line


def get_new_colours(colour_tree, linebot):
    colours = [colour_tree[x] for x in linebot if x != 0]  # todo
    new_colours = {0: 0, **remap_colours(colours)}
    recoloured_bot_line = [new_colours[colour_tree[x]] for x in linebot]
    return recoloured_bot_line


def count_based_on_four_vertices(bot_entry, top_entry, top_last_colour, bot_last_colour, colour_tree):
    counter = 0
    bot_active = bot_last_colour != 0
    top_active = top_last_colour != 0

    top_edge = top_entry and not top_active
    bot_edge = bot_entry and not bot_active

    if bot_edge:
        if top_active:
            colour_tree.join(bot_entry, top_last_colour)
        if top_entry:
            colour_tree.join(bot_entry, top_entry)
        if not top_active and not top_entry:
            counter += 1

    if top_edge:
        if bot_active:
            if colour_tree[bot_last_colour] != colour_tree[top_entry]:
                counter -= 1
            colour_tree.join(bot_last_colour, top_entry)
        elif bot_entry:
            if colour_tree[bot_entry] != colour_tree[top_entry]:
                counter -= 1
            colour_tree.join(bot_entry, top_entry)

    return counter


def ensure_negative_colours(linebot):
    return [-abs(x) for x in linebot]
