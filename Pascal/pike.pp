program ex3_1;
var
    s,t:integer;
begin
     s:=0;                 {S置初值为0}
     for t:=1 to 13 do     {For循环语句}
           s:=s+t;
     writeln('total:',s*4);
	end.
