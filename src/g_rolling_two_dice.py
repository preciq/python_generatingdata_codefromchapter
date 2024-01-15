"""Same as f_die_visual but for rolling 2 die and graphing their result"""

from e_die import Die
import plotly.express as px

# create 2 die (default 6 sides)
die1 = Die()
die2 = Die()

# roll and store the results
results = []
for i in range(0, 1000):
    # roll 1000 times and append each result to results list
    results.append(die1.roll() + die2.roll())

# analyze the results
frequencies = []
poss_results_on_die = range(2, die1.num_of_sides + die2.num_of_sides + 1)
# cumulatively storing the number of values possible from throwing 2 dies. Minimum number is 2 so starting from there (1 + 1 on each die)
for value in poss_results_on_die:
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)
# results appear something like this: [30, 61, 77, 105, 130, 186, 158, 91, 96, 40, 26]; i.e. 8 was rolled 91 times

# can use these to generate a chart called a histogram

fig = px.bar(
    x=poss_results_on_die,
    y=frequencies,
    title="Number of times a die value was rolled",
    labels={
        "x": "Die cumulative value",
        "y": "Frequency of value",
    },
    # hover_name=frequencies
    # can add hover elements using this, but need a list
)

fig.update_layout(xaxis_dtick=1)
# ensures that each bar has a label on the x axis (i.e. a score of 5 actually has a '5' on the x axis under it, clearly labelling it)

# generates a histogram with x as the various possible results (2 - 12 on 2 dies thrown together) and y as the number of times each result appears
fig.show()

# saves the generated diagram as an HTML file
fig.write_html('rolling_two_dice.html')