import codecademylib
import numpy as np
from matplotlib import pyplot as plt

survey_responses = ['Ceballos', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos','Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos']
total = len(survey_responses)
print(total)
total_ceballos = sum([1 for n in survey_responses if n=='Ceballos'])
print(total_ceballos)
percentage_ceballos = 100 * total_ceballos/len(survey_responses)
print(percentage_ceballos)
possible_surveys = np.random.binomial(total, 0.54, 10000) / total
print(possible_surveys)
plt.hist(possible_surveys, range=(0, 1), bins=20)
plt.title('Binomial Election Results')
plt.xlabel('Voter Percentage')
plt.ylabel('Frequency')
plt.show()

celabllos_loss_surveys = np.mean(possible_surveys < 0.5)
print(celabllos_loss_surveys)

large_survey = np.random.binomial(7000,0.54, 10000)/7000
print(large_survey)
ceballos_loss_new = np.mean(large_survey < 0.5)
print (ceballos_loss_new)
