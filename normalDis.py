import statistics
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go

data = pd.read_csv("StudentsPerformance.csv")

#sorting data into categories...
math_score = data["math score"].to_list()
reading_score = data["reading score"].to_list()
writing_score = data["writing score"].tolist()

#calculating mean, median and mode of math score, reading score & writing score...
math_score_mean = statistics.mean(math_score)
math_score_median = statistics.median(math_score)
math_score_mode = statistics.mode(math_score)

math_score_stdev = statistics.stdev(math_score)

print("Mean, Median and mode of MATH SCORE is - {}, {} and {}".format(math_score_mean, math_score_median, math_score_mode))

reading_score_mean = statistics.mean(reading_score)
reading_score_median = statistics.median(reading_score)
reading_score_mode = statistics.mode(reading_score)

reading_score_stdev = statistics.stdev(reading_score)

print("Mean, Median and mode of READING SCORE is - {}, {} and {}".format(reading_score_mean, reading_score_median, reading_score_mode))

writing_score_mean = statistics.mean(writing_score)
writing_score_median = statistics.mean(writing_score)
writing_score_mode = statistics.mean(writing_score)

writing_score_stdev = statistics.stdev(writing_score)

print("Mean, Median and mode of WRITING SCORE is - {}, {} and {}".format(writing_score_mean, writing_score_median, writing_score_mode))

math_score_first_stdev_strt, math_score_first_stdev_end = math_score_mean - math_score_stdev, math_score_mean + math_score_stdev
math_score_second_stdev_strt, math_score_second_stdev_end = math_score_mean - (math_score_stdev*2), math_score_mean + (math_score_stdev*2)
math_score_third_stdev_strt, math_score_third_stdev_end = math_score_mean - (math_score_stdev*3), math_score_mean + (math_score_stdev*3)

math_score_fig = ff.create_distplot([math_score],["Math Score Result"], show_hist=False)
math_score_fig.add_trace(go.Scatter(x=[math_score_mean,math_score_mean], y=[0,0.17], mode="lines", name="Mean"))

math_score_fig.add_trace(go.Scatter(x=[math_score_first_stdev_strt, math_score_first_stdev_strt], y=[0,0.17], mode="lines", name="First Start"))
math_score_fig.add_trace(go.Scatter(x=[math_score_first_stdev_end, math_score_first_stdev_end], y=[0,0.17], mode="lines", name="First End"))

math_score_fig.add_trace(go.Scatter(x=[math_score_second_stdev_strt, math_score_second_stdev_strt], y=[0,0.17], mode="lines", name="Second Start"))
math_score_fig.add_trace(go.Scatter(x=[math_score_second_stdev_end, math_score_second_stdev_end], y=[0,0.17], mode="lines", name="Second End"))

math_score_fig.add_trace(go.Scatter(x=[math_score_third_stdev_strt, math_score_third_stdev_strt], y=[0,0.17], mode="lines", name="Third Start"))
math_score_fig.add_trace(go.Scatter(x=[math_score_third_stdev_end, math_score_third_stdev_end], y=[0,0.17], mode="lines", name="Third End"))
math_score_fig.show()

list_of_math_score_within_first_stdev=[result for result in math_score if result>math_score_first_stdev_strt and result<math_score_first_stdev_end]
print("{} percent(%) of math score data lies within first standard dev.".format(len(list_of_math_score_within_first_stdev)*100/len(math_score)))

list_of_math_score_within_second_stdev=[result for result in math_score if result>math_score_second_stdev_strt and result<math_score_second_stdev_end]
print("{} percent(%) of math score data lies within second standard dev.".format(len(list_of_math_score_within_second_stdev)*100/len(math_score)))

list_of_math_score_within_third_stdev=[result for result in math_score if result>math_score_third_stdev_strt and result<math_score_third_stdev_end]
print("{} percent(%) of math score data lies within third standard dev.".format(len(list_of_math_score_within_third_stdev)*100/len(math_score)))



reading_score_first_stdev_strt, reading_score_first_stdev_end = reading_score_mean - reading_score_stdev, reading_score_mean + reading_score_stdev
reading_score_second_stdev_strt, reading_score_second_stdev_end = reading_score_mean - (reading_score_stdev*2), reading_score_mean + (reading_score_stdev*2)
reading_score_third_stdev_strt, reading_score_third_stdev_end = reading_score_mean - (reading_score_stdev*3), reading_score_mean + (reading_score_stdev*3)

reading_score_fig = ff.create_distplot([reading_score],["Reading Score Result"], show_hist=False)
reading_score_fig.add_trace(go.Scatter(x=[reading_score_mean,reading_score_mean], y=[0,0.17], mode="lines", name="Mean"))

reading_score_fig.add_trace(go.Scatter(x=[reading_score_first_stdev_strt, reading_score_first_stdev_strt], y=[0,0.17], mode="lines", name="First Start"))
reading_score_fig.add_trace(go.Scatter(x=[reading_score_first_stdev_end, reading_score_first_stdev_end], y=[0,0.17], mode="lines", name="First End"))

reading_score_fig.add_trace(go.Scatter(x=[reading_score_second_stdev_strt, reading_score_second_stdev_strt], y=[0,0.17], mode="lines", name="Second Start"))
reading_score_fig.add_trace(go.Scatter(x=[reading_score_second_stdev_end, reading_score_second_stdev_end], y=[0,0.17], mode="lines", name="Second End"))

reading_score_fig.add_trace(go.Scatter(x=[reading_score_third_stdev_strt, reading_score_third_stdev_strt], y=[0,0.17], mode="lines", name="Third Start"))
reading_score_fig.add_trace(go.Scatter(x=[reading_score_third_stdev_end, reading_score_third_stdev_end], y=[0,0.17], mode="lines", name="Third End"))
reading_score_fig.show()

list_of_reading_score_within_first_stdev=[result for result in reading_score if result>reading_score_first_stdev_strt and result<reading_score_first_stdev_end]
print("{} percent(%) of reading score data lies within first standard dev.".format(len(list_of_reading_score_within_first_stdev)*100/len(reading_score)))

list_of_reading_score_within_second_stdev=[result for result in reading_score if result>reading_score_second_stdev_strt and result<reading_score_second_stdev_end]
print("{} percent(%) of reading score data lies within second standard dev.".format(len(list_of_reading_score_within_second_stdev)*100/len(reading_score)))

list_of_reading_score_within_third_stdev=[result for result in reading_score if result>reading_score_third_stdev_strt and result<reading_score_third_stdev_end]
print("{} percent(%) of reading score data lies within third standard dev.".format(len(list_of_reading_score_within_third_stdev)*100/len(reading_score)))



writing_score_first_stdev_strt, writing_score_first_stdev_end = writing_score_mean - writing_score_stdev, writing_score_mean + writing_score_stdev
writing_score_second_stdev_strt, writing_score_second_stdev_end = writing_score_mean - (writing_score_stdev*2), writing_score_mean + (writing_score_stdev*2)
writing_score_third_stdev_strt, writing_score_third_stdev_end = writing_score_mean - (writing_score_stdev*3), writing_score_mean + (writing_score_stdev*3)

writing_score_fig = ff.create_distplot([writing_score],["Writing Score Result"], show_hist=False)
writing_score_fig.add_trace(go.Scatter(x=[writing_score_mean,writing_score_mean], y=[0,0.17], mode="lines", name="Mean"))

writing_score_fig.add_trace(go.Scatter(x=[writing_score_first_stdev_strt, writing_score_first_stdev_strt], y=[0,0.17], mode="lines", name="First Start"))
writing_score_fig.add_trace(go.Scatter(x=[writing_score_first_stdev_end, writing_score_first_stdev_end], y=[0,0.17], mode="lines", name="First End"))

writing_score_fig.add_trace(go.Scatter(x=[writing_score_second_stdev_strt, writing_score_second_stdev_strt], y=[0,0.17], mode="lines", name="Second Start"))
writing_score_fig.add_trace(go.Scatter(x=[writing_score_second_stdev_end, writing_score_second_stdev_end], y=[0,0.17], mode="lines", name="Second End"))

writing_score_fig.add_trace(go.Scatter(x=[writing_score_third_stdev_strt, writing_score_third_stdev_strt], y=[0,0.17], mode="lines", name="Third Start"))
writing_score_fig.add_trace(go.Scatter(x=[writing_score_third_stdev_end, writing_score_third_stdev_end], y=[0,0.17], mode="lines", name="Third End"))
writing_score_fig.show()

list_of_writing_score_within_first_stdev=[result for result in writing_score if result>writing_score_first_stdev_strt and result<writing_score_first_stdev_end]
print("{} percent(%) of writing score data lies within first standard dev.".format(len(list_of_writing_score_within_first_stdev)*100/len(writing_score)))

list_of_writing_score_within_second_stdev=[result for result in writing_score if result>writing_score_second_stdev_strt and result<writing_score_second_stdev_end]
print("{} percent(%) of writing score data lies within second standard dev.".format(len(list_of_writing_score_within_second_stdev)*100/len(writing_score)))

list_of_writing_score_within_third_stdev=[result for result in writing_score if result>writing_score_third_stdev_strt and result<writing_score_third_stdev_end]
print("{} percent(%) of writing score data lies within third standard dev.".format(len(list_of_writing_score_within_third_stdev)*100/len(writing_score)))