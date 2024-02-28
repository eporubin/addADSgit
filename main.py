#reading from input file
f = open('input.txt')
raw_lines = f.readlines()
lines = [x.rstrip() for x in raw_lines]

#reading from the target
t = open('target.txt')
t_raw_lines = t.readlines()
t_lines = [x.rstrip() for x in t_raw_lines]



end_line = t_lines.index("! $document blocks") 
print(end_line)

block_list = t_lines[1:end_line]
for line in block_list[:10]:
    print(line)

result_list = sorted(list(set(lines + block_list)))

o = open("output.txt","w")
o.write(t_lines[0] + "\n")
for line in result_list:
    o.write(line + "\n")
for line in t_lines[end_line:]:
    o.write(line + "\n")