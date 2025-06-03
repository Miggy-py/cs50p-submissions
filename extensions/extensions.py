def main():

    user_file = input("File name: ").strip().lower()

    output = get_file_output(user_file)

    print(output)


def get_file_output(user_file):
    output = ""
    types = {"gif": "image",
             "jpg": "image",
             "jpeg": "image",
             "png": "image",
             "pdf": "application",
             "txt": "text",
             "zip": "application"
            }

    partitioned = user_file.rpartition(".")
    extension = partitioned[2]

    if not partitioned[0] or extension not in types:
        output = "application/octet-stream"
        return output

    type = types[extension]

    if(type == "image"):
        if(extension == "jpg" or extension == "jpeg"):
            output = "image/jpeg"
        else:
            output = "image/" + extension

    elif(type == "application"):
        output = "application/" + extension

    elif(type == "text"):
        output = type + "/" + partitioned[0]

    else:
        output = "application/octet-stream"

    return output


if __name__ == "__main__":
    main()
