# regularPolygonalLimit

## problem definition

```
반지름이 1(r1)인 원(c1)이 있다.
c1에 외접하는 정삼각형(s3)을 그린다. s3에 외접하는 원(c2)를 그린다.
c2에 외접하는 정사각형(s4)를 그린다. s4에 외접하는 원(c3)를 그린다.
c3에 외접하는 정오각형(s5)를 그린다. s5에 외접하는 원(c4)를 그린다.
.
.
c(n)에 외접하는 s(n+2)를 그린다. s(n+2)에 외접하는 c(n+1)를 그린다.
.
.
시작 원c(1)의 radius가 r(1)=1 일 때,  lim(x->inf)c(x)는 어떻게 거동하는가?
수렴한다면 어떤 수치에 수렴하는가?%
```

## figure
![Alt text](example.png "when n=20")

## result
```
약 8.7000366476에 수렴한다.
```