st = "This is fine. That is also fine"
freq = {}
for w in st.split():
    w = w.strip('.')
    if w in freq:
        freq[w] = freq[w] + 1
    else:
        freq[w] = 1

for w, f in freq.items():
    print(w, f)
