def shut_down(s:str)->str:
    if s == "yes":
         return "Shutting down" 
    if s == "no":
        return "Shutting aborted"
    else:
        return "Sorry"


shut_down("hello")
        "