l =["SPAN","IMSM"]
K = """
    SELECT * FROM CI050
    WHERE timeofday IN
    (SELECT MIN(timeofday)
    FROM CI050) AND margin_type IN """ + str(set(l))
print(K)