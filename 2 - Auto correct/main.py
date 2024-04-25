from get_words import get_words
from model.pre_process import pre_process


def main():
	gw = get_words()
	pr = pre_process()
	lng_input = input("please enter a langauge  (en / fa) : ")

	while lng_input.lower() not in ["en", "fa"]:
		lng_input = input("please enter a langauge : (en / fa) : ")

	text = input("please enter words : ")
	text = pr.process(text, lng_input)

	result = gw.get(text, lng_input)

	


	print("		edit distance model		")
	for index, word in enumerate(result["edit distance"]):
		print(f"		 {index + 1}----> {word}")

	print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

	print("		jaccard similarity model		")
	for index, word in enumerate(result["jaccard similarity"]):
		print(f"		 {index + 1}----> {word}")

main()

