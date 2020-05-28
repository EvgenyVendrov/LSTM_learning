import os

dest_path = r"C:\Users\evgen\Desktop\LSTM TRYING\data-set"
src_path = r"C:\Users\evgen\Desktop\LSTM TRYING\linux-master"
wanted_file_postfix = "c"
whole_data = ""
counting_files = 0
did_fail = False

for root, dirs, files in os.walk(src_path):
    if counting_files > 10:
        break
    for file in files:
        if file.endswith(wanted_file_postfix):
            path = os.path.join(root, file)
            with open(path, "r", encoding="utf8") as f:
                print("copying ", file, "....")
                try:
                    whole_data += f.read()
                except:
                    did_fail = True
                    print(file, "wont be copied - not utf-8")
                if not did_fail:
                    counting_files += 1
                    print("finished")
                did_fail = False

print("finished copying ", counting_files, " files")
print("starting to write to ", dest_path + "\whole_data_set.txt")
with open(dest_path + "\whole_data_set.txt", "w", encoding="utf8") as f:
    f.write(whole_data)

print("finished :)")
