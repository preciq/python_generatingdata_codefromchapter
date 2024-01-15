from e_die import Die
import plotly.express as px

# create a die (default 6 sides)
die = Die()

# roll and store the results
results = []
for i in range(0, 1000):
    # roll 1000 times and append each result to results list
    results.append(die.roll())

# analyze the results
frequencies = []
poss_results_on_die = range(1, die.num_of_sides + 1)
for value in poss_results_on_die:
    # looping through the side numbers (the 1, 2, 3... on the dice itself)
    frequency = results.count(value)
    # count the number of times a value appears in the results of throwing the dice
    frequencies.append(frequency)
    # append this value to the frequency array. Results are in order, so the first number appended to frequencies represents how many times '1' was rolled, second number represents how many times '2' was rolled, etc.

print(frequencies)
# results appear something like this: [176, 167, 152, 169, 168, 168]; i.e. 1 was rolled 176 times

# can use these to generate a chart called a histogram

fig = px.bar(
    x=poss_results_on_die, 
    y=frequencies,
    title="Number of times a die value was rolled",
    labels= {
        "x": "Die value",
        "y": "Frequency of value",
        },
    )
# generates a histogram with x as the various possible results (1, 2, 3, 4, 5, 6 on a 6 sided die) and y as the number of times each result appears
fig.show()