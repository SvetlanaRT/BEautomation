# class Tweet:
#     pass
#
# a = Tweet()
#
# a.message = '140 characters'
#
# print(a.message)
# ------------------------------------
# class init:
#
#     def __init__(self):             #__init__ created to perform some action immediately when object created

#      print('Hi')      #self allow you to custom constructor without adding any argument if you don't want to
#
# a=init()
# -------------------------------------
# class Arguments:
#     def __init__(self, argument2):
#         self.attribute = argument2
#         print(self.attribute)
#         print(argument2)
#         self.attribute = "another text not argument2"
#         print(self.attribute)
#
#
# a = Arguments("some text")
# -------------------------------------
class Example:
    def __init__(self, message):
        self.message = message  # attribure 'message' of any instance/object of will be = ....(meaning of 'self')
