# PeopleCare

## Problem Description

PeopleCare is an Insurance company that provides Health Insurance to its customers. They have successfully moved up the market ladder and become popular within a span of a few years. Now the company has decided to expand its insurance to vehicles as well. They want to optimize their cost of reaching out to customers by only focusing on customers who have a higher likelihood of purchasing the vehicle policy.

Now, in order to predict whether a customer would be interested in Vehicle insurance, PeopleCare has conducted a public survey and collected information about demographics (gender, age, region code type), Vehicles (Vehicle Age, Damage), Policy (Premium, sourcing channel) etc. They have hired you as a data scientist to build a model to predict whether these potential customers would be interested in opting for a Vehicle Insurance from PeopleCare. They will only use this strategy if you are able to create a model which is atleast 75% accurate.

| **Variable** | **Definition** |
| --- | --- |
| id | Unique ID for the customer |
| Gender | Gender of the customer |
| Age | Age of the customer |
| Driving\_License | 0 : Customer does not have DL, 1 : Customer already has DL |
| Region\_Code | Unique code for the region of the customer |
| Previously\_Insured | 1 : Customer already has Vehicle Insurance, 0 : Customer doesn't have Vehicle Insurance |
| Vehicle\_Age | Age of the Vehicle  |
| Vehicle\_Damage | 1 : Customer got his/her vehicle damaged in the past. 0 : Customer didn't get his/her vehicle damaged in the past. |
| Annual\_Premium | The amount customer needs to pay as premium in the year |
| Policy\_Sales\_Channel | Anonymised Code for the channel of outreaching to the customer ie. Different Agents, Over Mail, Over Phone, In Person, etc. |
| Vintage | Number of Days, Customer has been associated with the company |
| Response | 1 :  Customer is interested, 0 : Customer is not interested |