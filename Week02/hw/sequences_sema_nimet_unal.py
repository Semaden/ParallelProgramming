my_list = [3, 9, 7, 9, 1, 1, 7, 397]
my_tuple = (12, 17, "Gentleman Thief", "Lupın")
my_set = {"Arsen Lupen", "Assane Diop", "Mariama Diop", "Claire", "Raul", "Raul"}
my_dict = {1:"Fais", 2:"ce", 3:"que", 4:"veux",
}

def remove_duplicates(seq: list) -> list:
return list(set(seq))

def list_counts(seq: list) -> dict:
return {item: seq.count(item) for item in set(seq)}

def reverse_dict(d: dict) -> dict:
return {value: key for key, value in d.items()}
