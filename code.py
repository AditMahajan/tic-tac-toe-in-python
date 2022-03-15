theBoard = {&#39;7&#39;: &#39; &#39; , &#39;8&#39;: &#39; &#39; , &#39;9&#39;: &#39; &#39; ,
&#39;4&#39;: &#39; &#39; , &#39;5&#39;: &#39; &#39; , &#39;6&#39;: &#39; &#39; ,
&#39;1&#39;: &#39; &#39; , &#39;2&#39;: &#39; &#39; , &#39;3&#39;: &#39; &#39; }

board_keys = []

for key in theBoard:
board_keys.append(key)

def printBoard(board):
print(board[&#39;7&#39;] + &#39;|&#39; + board[&#39;8&#39;] + &#39;|&#39; + board[&#39;9&#39;])
print(&#39;-+-+-&#39;)
print(board[&#39;4&#39;] + &#39;|&#39; + board[&#39;5&#39;] + &#39;|&#39; + board[&#39;6&#39;])
print(&#39;-+-+-&#39;)
print(board[&#39;1&#39;] + &#39;|&#39; + board[&#39;2&#39;] + &#39;|&#39; + board[&#39;3&#39;])

#gameplay functionality
def game():

turn = &#39;X&#39;
count = 0

for i in range(10):
printBoard(theBoard)
print(&quot;It&#39;s your turn,&quot; + turn + &quot;.Move to which place?&quot;)

move = input()

if theBoard[move] == &#39; &#39;:
theBoard[move] = turn
count += 1
else:
print(&quot;That place is already filled.\nMove to which place?&quot;)
continue
if count &gt;= 5:
if theBoard[&#39;7&#39;] == theBoard[&#39;8&#39;] == theBoard[&#39;9&#39;] != &#39; &#39;:

printBoard(theBoard)
print(&quot;\nGame Over.\n&quot;)
print(&quot; **** &quot; +turn + &quot; won. ****&quot;)
break
elif theBoard[&#39;4&#39;] == theBoard[&#39;5&#39;] == theBoard[&#39;6&#39;] != &#39; &#39;:
printBoard(theBoard)
print(&quot;\nGame Over.\n&quot;)
print(&quot; **** &quot; +turn + &quot; won. ****&quot;)
break
elif theBoard[&#39;1&#39;] == theBoard[&#39;2&#39;] == theBoard[&#39;3&#39;] != &#39; &#39;:
printBoard(theBoard)
print(&quot;\nGame Over.\n&quot;)
print(&quot; **** &quot; +turn + &quot; won. ****&quot;)
break
elif theBoard[&#39;1&#39;] == theBoard[&#39;4&#39;] == theBoard[&#39;7&#39;] != &#39; &#39;:
printBoard(theBoard)
print(&quot;\nGame Over.\n&quot;)
print(&quot; **** &quot; +turn + &quot; won. ****&quot;)
break
elif theBoard[&#39;2&#39;] == theBoard[&#39;5&#39;] == theBoard[&#39;8&#39;] != &#39; &#39;:
printBoard(theBoard)
print(&quot;\nGame Over.\n&quot;)
print(&quot; **** &quot; +turn + &quot; won. ****&quot;)
break
elif theBoard[&#39;3&#39;] == theBoard[&#39;6&#39;] == theBoard[&#39;9&#39;] != &#39; &#39;:
printBoard(theBoard)
print(&quot;\nGame Over.\n&quot;)
print(&quot; **** &quot; +turn + &quot; won. ****&quot;)
break
elif theBoard[&#39;7&#39;] == theBoard[&#39;5&#39;] == theBoard[&#39;3&#39;] != &#39; &#39;:

printBoard(theBoard)
print(&quot;\nGame Over.\n&quot;)
print(&quot; **** &quot; +turn + &quot; won. ****&quot;)
break
elif theBoard[&#39;1&#39;] == theBoard[&#39;5&#39;] == theBoard[&#39;9&#39;] != &#39; &#39;:
printBoard(theBoard)
print(&quot;\nGame Over.\n&quot;)
print(&quot; **** &quot; +turn + &quot; won. ****&quot;)
break

if count == 9:
print(&quot;\nGame Over.\n&quot;)
print(&quot;It&#39;s a Tie!!&quot;)

if turn ==&#39;X&#39;:
turn = &#39;O&#39;
else:
turn = &#39;X&#39;

restart = input(&quot;Do want to play Again?(y/n)&quot;)
if restart == &quot;y&quot; or restart == &quot;Y&quot;:
for key in board_keys:
theBoard[key] = &quot; &quot;

game()

if __name__ == &quot;__main__&quot;:
game()
