import pandas as pd


def labels_to_csv(labels_path, output_filename):
    labels = open(labels_path).read().split("\n\n")
    fields = ("Q_NAME", "Description", "Option_Num", "Option_Text")
    data = []
    for label in labels:
        strings = label.split("\n")
        if not strings[0]:
            strings = strings[1:]
        if len(strings) <= 5:
            continue
        Q_NAME = strings[0].split(") ")[1]
        descr = strings[1]
        for option in strings[5:]:
            if ")" not in option:
                break
            option = option.split("\t")[0]
            br_ix = option.index(")")
            opt_num = option[:br_ix]
            opt_text = option[br_ix + 2:]
            data.append((Q_NAME, descr, opt_num, opt_text))
    pd.DataFrame([fields] + data).to_csv(output_filename, index=False, header=False)
    


if __name__ == "__main__":
    for i in range(2014, 2023):
        if i != 2020:
            labels_to_csv(f"data/csaf_{i}_labels.txt", f"data/csaf_{i}_labels.csv")