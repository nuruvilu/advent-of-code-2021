-module(part1).
-export([doproblem/0]).

openners(40) -> 41;
openners(91) -> 93;
openners(123) -> 125;
openners(60) -> 62;
openners(_) -> nope.

points(41) -> 3;
points(93) -> 57;
points(125) -> 1197;
points(62) -> 25137. 

score(<<>>, _) -> 0;
score(<<Char, Chars/binary>>, []) ->
    case openners(Char) of
        nope -> points(Char);
        _ -> score(Chars, [Char])
    end;
score(<<Char, Chars/binary>>, Stack = [SHead | STail]) ->
    case openners(Char) of
        nope ->
            case openners(SHead) of
                N when N =:= Char -> score(Chars, STail);
                N when N =/= Char -> points(Char)
            end;
        _ -> score(Chars, [Char | Stack])
    end.


solve(List) ->
    Scores = lists:map(fun(S) -> score(S, []) end, List),
    lists:sum(Scores).

doproblem() ->
    {ok, Text} = file:read_file("input.txt"),
    solve(string:split(string:trim(Text), "\n", all)).
