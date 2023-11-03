url = input("\n\nEnter GitHub Repo URL : ")

try:
    if url[-1] == "/":
        repo_name = url.split("/")[-2]
        user_name = url.split("/")[-3]
    else:
        repo_name = url.split("/")[-1]
        user_name = url.split("/")[-2]

except:
    print("\nSomething went wrong, please try again.")
    exit()

category = input(("\n\nEnter Repo Category : "))

description = input(("\n\nEnter Repo Description : "))

with open("README.md", "r") as file:
    text = file.readlines()
    last_entry = text[-6]
    last_index = int(last_entry.split(".")[0])
    index = last_index + 1


new_line = f"{str(index)}.| [{repo_name}]({url}) | {category} | ![GitHub Repo stars](https://img.shields.io/github/stars/{user_name}/{repo_name}?style=social) | {description}"

text.insert(-5, new_line)
text.insert(-4, "\n")
text = "".join(text)  # Join list with delimiter \n

with open("README.md", "w") as file:
    print("\n\n\nUpdating README.md")
    file.write(text)
    print("\nCompleted.\n")
