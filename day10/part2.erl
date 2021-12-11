-module(part2).
-export([doproblem/0]).

openners(40) -> 41;
openners(91) -> 93;
openners(123) -> 125;
openners(60) -> 62;
openners(_) -> nope.

points(41) -> 1;
points(93) -> 2;
points(125) -> 3;
points(62) -> 4. 

score(<<>>, Stack) -> 
    lists:foldl(fun(C, Acc) -> Acc * 5 + points(openners(C)) end, 0, Stack);
score(<<Char, Chars/binary>>, []) ->
    case openners(Char) of
        nope -> corrupt;
        _ -> score(Chars, [Char])
    end;
score(<<Char, Chars/binary>>, Stack = [SHead | STail]) ->
    case openners(Char) of
        nope ->
            case openners(SHead) of
                N when N =:= Char -> score(Chars, STail);
                N when N =/= Char -> corrupt
            end;
        _ -> score(Chars, [Char | Stack])
    end.

solve(List) ->
    Scores = lists:map(fun(S) -> score(S, []) end, List),
    Sorted = lists:sort(lists:filter(fun(S) -> S =/= corrupt end, Scores)),
    MidIndex = length(Sorted) div 2 + 1,
    case length(Sorted) of
        N when N rem 2 =:= 1 -> lists:nth(MidIndex, Sorted);
        N when N rem 2 =:= 0 ->
            (lists:nth(MidIndex, Sorted) + lists:nth(MidIndex + 1, Sorted)) / 2
    end.

doproblem() ->
    {ok, Text} = file:read_file("input.txt"),
    solve(string:split(string:trim(Text), "\n", all)).
