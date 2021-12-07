-module(part1).
-export([doproblem/0]).

count_increasing([Read | [Next_Read | _] = Reads], Sum) when Next_Read > Read ->
    count_increasing(Reads, Sum + 1);
count_increasing([Read | [Next_Read | _] = Reads], Sum) when Next_Read =< Read ->
    count_increasing(Reads, Sum);
count_increasing(_, Sum) ->
    Sum.

solve(List) ->
    Reads = lists:map(fun string:to_integer/1, List),
    count_increasing(Reads, 0).

doproblem() ->
    {ok, Text} = file:read_file("input.txt"),
    solve(string:split(Text, "\n", all)).
