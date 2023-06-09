def char_count(str):
  str = [*str]
  str = sorted(str)
  str = ''.join(str)
  answer = []
  log = []
  for elem in str:
    if elem == ' ':
      continue
    elif elem not in log:
      answer.append([elem, 1])
      log.append(elem)
    elif elem in log:
      answer[log.index(elem)][1] += 1
  answer.sort(key = lambda x : x[1], reverse=True)
    
  return answer