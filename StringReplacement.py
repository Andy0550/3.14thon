# Michael Dvořák
# Python_3.7.0

text="uace dxua s knpanlgq pweswm, zgnve n xuapewep, zeso sap zeswm, uiew ksam s fdsnaq sap cdwnudh iuvdke ub buwluqqea vuwe. zgnve n auppep, aeswvm asxxnal, hdppeavm qgewe cske s qsxxnal. sh ub huke uae leaqvm wsxxnal, wsxxnal sq km cgskyew puuw. qgnh huke inhnquw, n kdqqewep, qsxxnal sq km cgskyew puuw. uavm qgnh sap auqgnal kuwe."

table = [('a', 's'), ('b', 'y'), ('c', 'c'), ('d', 'p'), ('e', 'e'), ('f', 'b'),

('g', 'l'), ('h', 'g'), ('i', 'n'), ('j', 'r'), ('k', 'o'), ('l', 'v'),

('m', 'k'), ('n', 'a'), ('o', 'u'), ('p', 'x'), ('q', 'f'), ('r', 'w'),

('s', 'h'), ('t', 'q'), ('u', 'd'), ('v', 'i'), ('w', 'z'), ('x', 't'),

('y', 'm'), ('z', 'j')]


def replace(x,table):
    for i in table:
        if x == i[1]:    
            return i[0]
    return x
        
        
for y in text:
    print(replace(y,table),end = "")
            
