from hmstime import toseconds

data = (
   ("1h 1m 1s", 3600 + 60 + 1),
   ("2h", 7200),
   ("30m", 30 * 60),
   ("1m 59s", 119),
   ("30s", 30)
)

def test():
   for h, s in data:
      assert toseconds(h) == s
