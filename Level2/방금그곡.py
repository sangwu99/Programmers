def solution(m, musicinfos):
    answer = "(None)"
    answer_len = 0
    music_dict = {}
    for i in musicinfos:
        i = i.split(',')
        time = (int(i[1].split(':')[0])*60 + int(i[1].split(':')[1])) - (int(i[0].split(':')[0])*60 + int(i[0].split(':')[1]))
        basic = i[3].replace("C#","1").replace("D#","2").replace("F#","3").replace("G#","4").replace("A#","5")
        songs = basic*(1440//len(basic))
        music_dict[i[2]] = songs[:time+1]
    m = m.replace("C#","1").replace("D#","2").replace("F#","3").replace("G#","4").replace("A#","5")
    for j,k in music_dict.items():
        if (m in k) and (len(k)>answer_len):
            answer_len = len(k)
            answer = j
    return answer