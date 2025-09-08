# import pandas as pd

# data = {
#     "user_id": [1, 2, 3, 4, 5, 6, 7],
#     "name": ["Winston", "Jonathan", "Annabelle", "Sally", "Marwan", "David", "Shapiro"],
#     "mail": ["winston@leetcode.com", "jonathanisgreat", "bella-@leetcode.com",
#              "sally.come@leetcode.com", "quarz#2020@leetcode.com", "david69@gmail.com",
#              ".shapo@leetcode.com"]
# }

# df = pd.DataFrame(data)

# mask = (df["mail"]) & (df["mail"].str.endswith("@leetcode.com"))
# print(df)
# print(df[mask])



import pandas as pd

# Sample Users table
data = {
    "user_id": [1, 2, 3, 4, 5, 6, 7],
    "name": ["Winston", "Jonathan", "Annabelle", "Sally", "Marwan", "David", "Shapiro"],
    "mail": ["winston@leetcode.com", "jonathanisgreat", "bella-@leetcode.com",
             "sally.come@leetcode.com", "quarz#2020@leetcode.com", "david69@gmail.com",
             ".shapo@leetcode.com"]
}

df = pd.DataFrame(data)

# Condition 1: email ends with "@leetcode.com"
ends_with_domain = df["mail"].str.endswith("@leetcode.com")

# Condition 2: first character before "@" is a letter
first_char = df["mail"].str.split("@").str[0].str[0]
starts_with_letter = first_char.str.isalpha()

# Apply both conditions
valid_emails = df[ends_with_domain & starts_with_letter]

print(valid_emails)
