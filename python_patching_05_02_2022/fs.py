from subprocess import check_output

# returns the content of the code directory
def print_content_of_cwd():
    return check_output(['ls']).split() # this is the function we are mocking -- check_output() from subprocess package