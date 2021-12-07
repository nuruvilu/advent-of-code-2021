-module(part1).
-export([doproblem/0]).

fuel(X, Positions) ->
    lists:sum(lists:map(fun(Y) -> abs(X - Y) end, Positions)).

solve(List) ->
    Reads = lists:map(fun(X) -> {Y, _} = string:to_integer(X), Y end, List),
    Possibilities = lists:seq(lists:min(Reads), lists:max(Reads)),
    lists:min(lists:map(fun(X) -> fuel(X, Reads) end, Possibilities)).

doproblem() ->
    {ok, Text} = file:read_file("input.txt"),
    solve(string:split(string:trim(Text), ",", all)).
