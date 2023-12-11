boat_side="Right"
m_on_right=3
c_on_right=3
m_on_left=0
c_on_left=0
print("M=",m_on_left,"C=",c_on_left,"|----B|","M=",m_on_right,"C=",c_on_right)
while True:
    missionaries=int(input("No of missionaries or enter 10 to quit"))
    if missionaries==10:
        print('You Quit. Game Over!')
        break
    cannibals=int(input("No of cannibals:"))
    if ((missionaries+cannibals)!=1 and (missionaries+cannibals)!=2):
        print('Invalid Input')
        continue

    if boat_side=="Right":
        if(m_on_right<missionaries) or(c_on_right<cannibals):
            print('Invalid Input')

        m_on_right =m_on_right - missionaries
        c_on_right = c_on_right - cannibals

        m_on_left += missionaries
        c_on_left += cannibals

        print("M=", m_on_left, "C=", c_on_left, "|----B|", "M=", m_on_right, "C=", c_on_right)
        boat_side="Left"
    else:
        if (m_on_left < missionaries) or (c_on_left < cannibals):
            print('Invalid Input')

        m_on_left = m_on_left - missionaries
        c_on_left = c_on_left - cannibals

        m_on_right += missionaries
        c_on_right += cannibals

        print("M=", m_on_left, "C=", c_on_left, "|----B|", "M=", m_on_right, "C=", c_on_right)
        boat_side = "Right"

    if (m_on_right <c_on_right and m_on_right > 0) or (m_on_left < c_on_left and m_on_left > 0):
        print('You Loose!')
        break

    if(m_on_left==3) and(c_on_left==3):
        print('You Win!')
        break



