def SecsToHrsMnsSec(seconds):
    hrs=seconds//3600
    mns=(seconds%3600)//60
    secs=(seconds%3600)%60
    return f"[{hrs:02d}:{mns:02d}:{secs:02d}]"
    #return "%02i:%02i:02i" % (hrs,mns,seconds)
s=28863

s=(s+1)%24*60*60
print(s)
print(SecsToHrsMnsSec(s))