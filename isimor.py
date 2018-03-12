def isIsomorphic(s,t):
  s_dict={}
  t_dict={}
  for i in range(len(s)):
    if s[i] in s_dict.keys() and s_dict[s_[i]]!=t[i]:
      return False
    if t[i] in t_dict.keys() and t_dict[t[i]]!=s[i]:
      return False
    s_dict[s[i]]=t[i]
    t_dict[t[i]]=s[i]
  return True
