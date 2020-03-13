import random


'''
math
'''
def sign_activation(x):
	return 1 if x > 0 else -1


'''
A perceptron is the simplest neural network possible
A perceptron consists of one or more inputs, a processor, and a single output.

'''
class Perceptron:

	def __init__(self, x):
		self.weights = []

		for _ in range(x):
			self.weights.append(random.random())
		# print("inside const- weights = ")
		# print(self.weights)

	def print_weights(self):
		for x in self.weights:
			print(x)

	def feedforward(self, inputs):
		sum = 0
		for i, input in enumerate(inputs):
			sum += input*self.weights[i]
			# print(input,"*",self.weights[i],"=",input*self.weights[i])
		# print("sum = ", sum)
		return sign_activation(sum)



x = Perceptron(3)
# x.print_weights()

print(x.feedforward([50,-23,1]))



















