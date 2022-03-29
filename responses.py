def response(txt):
    usermsg=str(txt).lower()
    if usermsg in ('hi','hello','HELLO','مرحبا','salut'):
        return 'HI Welcome ! How Are You ?😉🤩'
    if usermsg in ('who are you?', 'who', 'who are you'):
        return 'I am PythonChat Bot AND You?🤪 '

    return 'I do not Understand what you Want 🤔🤔😵'