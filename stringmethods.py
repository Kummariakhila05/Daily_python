a="akki!!!!!! @@@ akki"
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("akki", "akhila"))
print(a.split(" "))

capital="introduction to python"
print(capital.capitalize())

stri="introduction to python"
print(len(stri))
print(stri.center(40))
print(a.count("akki"))

stri="introduction to python"
print(len(stri))

example="introduction to python!!!"
print(example.endswith("!!!"))

example1="introduction to python!!!"
print(example1.endswith("to", 9,15))  #trueconditionofendswith

example1="introduction to python!!!"
print(example1.endswith("to", 9,16))  #falseconditionofendswith

course="introduction to javascript"
print(course.find("to"))

course="introduction to javascript"
print(course.isalnum())

course="introductiontojavascript"
print(course.isalpha())

course="introduction to javascript\n" #falsecondn
print(course.isprintable())

course="introduction to javascript"  #truecondn
print(course.isprintable())

course="           "
print(course.isspace())

course="introduction to javascript"
print(course.title())