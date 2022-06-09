# [KT_icpcawards](https://open.kattis.com/problems/icpcawards)

* en

  ```en

  ```

* kr

  ```kr
  첫 줄에는 N, 다음 N 줄엔 대학이름 팀이름이 순위대로 주어진다
  상을 받는 상위 12팀 이름을 출력하라, 단 한 대학에서는 한 팀만 상을 받을 수 있다
  ```

* tc

  ```tc
  Input:
  30
  Seoul ACGTeam
  VNU LINUX
  SJTU Mjolnir
  VNU WINDOWS
  NTU PECaveros
  HUST BKJuniors
  HCMUS HCMUSSerendipity
  VNU UBUNTU
  SJTU Metis
  HUST BKDeepMind
  HUST BKTornado
  HCMUS HCMUSLattis
  NUS Tourism
  VNU DOS
  HCMUS HCMUSTheCows
  VNU ANDROID
  HCMUS HCMUSPacman
  HCMUS HCMUSGeomecry
  UIndonesia DioramaBintang
  VNU SOLARIS
  UIndonesia UIChan
  FPT ACceptable
  HUST BKIT
  PTIT Miners
  PSA PSA
  DaNangUT BDTTNeverGiveUp
  VNU UNIXBSD
  CanTho CTUA2LTT
  Soongsil Team10deung
  Soongsil BezzerBeater

  Output:
  Seoul ACGTeam
  VNU LINUX
  SJTU Mjolnir
  NTU PECaveros
  HUST BKJuniors
  HCMUS HCMUSSerendipity
  NUS Tourism
  UIndonesia DioramaBintang
  FPT ACceptable
  PTIT Miners
  PSA PSA
  DaNangUT BDTTNeverGiveUp
  ```

## Solution

* py

  ```py
  N = int(input())
  seen = set()
  for _ in range(N):
    uni, team = input().split()
    if uni not in seen and len(seen) < 12:
      print(uni, team)
    seen.add(uni)
  ```
