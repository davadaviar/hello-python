full_dot = '●'
empty_dot = '○'

def create_character(name, strength, intelligence, charisma, max_stat = 10):

    # name validated
    if not isinstance(name, str):
        return 'The character name should be a string'
    if name == '':
        return 'The character should have a name'
    if len(name) > 10:
        return 'The character name is too long'
    if ' ' in name:
        return 'The character name should not contain spaces'

    # any stats validated
    if not isinstance(strength, int) or not isinstance(intelligence, int) or not isinstance(charisma, int):
        return 'All stats should be integers.'
    
    stat_sum = strength + intelligence + charisma

    # stats range validated
    if strength < 1 or intelligence < 1 or charisma < 1:
        return 'All stats should be no less than 1.'
    if strength > 4 or intelligence > 4 or charisma > 4:
        return 'All stats should be no more than 4.'
    if stat_sum != 7:
        return 'The character should start with 7 points.'

    # stats
    def stat_bar(value, max_bar = max_stat):
        filled = value * full_dot
        empty = (max_bar - value) * empty_dot
        return filled + empty

    return f'Name: {name}\nStrength: {stat_bar(strength)}\nIntelligence: {stat_bar(intelligence)}\nCharisma: {stat_bar(charisma)}'

print(create_character('ren', 4, 2, 1))
