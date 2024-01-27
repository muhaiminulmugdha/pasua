print("Passwords")

password = input("whats the pass: ")

if password == "mugdho":

  cs2_students = {"email": " sishafique1962@gmail.com \n pass: TANGAIL1962",
      "email2": " madmiah062@gmail.com \n pass: TANGAIL1962", 
      "ebt": " selinaakterh1979@gmail.com \n pass: mumu98mugdho06$" , 
      "riseup": "sishafique1962@gmail.com \n pass: sHafiquE&&$$1 \n pin: 3031", 
      "citizenmd": "sishafique1962@gmail.com \n pass: TANGAIL1962 ",
      "citizense": "selinaakterh1979@gmail.com \n pass: mumu98mugdha06$ ", 
      }


  compnumb = input("WHAT DO YOU WANT TO KNOW: ")
  compnumb = str(compnumb)




  def find_cs2_students(ques, student_list):
      if ques in student_list:
          return (student_list[ques])
      else:
          return (f"we dont have{ques} in our list")



  """
  //pseudocode
  var = input
  while (var == true):
  do stuff
  var = input

  OR

  while True:
  do stuff
  if input == 'quit':
  break;


  """

  print(find_cs2_students(compnumb, cs2_students))


  askk = input("Do you want to know anything else: ")
  while (askk == "yes"):
      compnumb = input("WHAT DO YOU WANT TO KNOW: ")
      compnumb = str(compnumb)
      print(find_cs2_students(compnumb, cs2_students))
      askk = input("Do you want to know anything else: ")
  else:
      print("WE DON'T HAVE IT IN OUR LIST")
else:
    print("wrong pass")
