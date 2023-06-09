li_in = [1,2,3,4]


def Split(mix):
    ev_li = [ele for ele in li_in if ele % 2 == 0]
    od_li = [ele for ele in li_in if ele % 2 != 0]
    print("Even lists:", ev_li)
    print("Odd lists:", od_li)


# Driver Code
mix = [2, 5, 13, 17, 51, 62, 73, 84, 95]
Split(mix)