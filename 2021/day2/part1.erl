-module(part1).
-export([doproblem/0]).


depthstance([], Depth, Length) ->
    Depth * Length;
depthstance([[<<"forward">>, Mag] | Moves], Depth, Length) ->
    depthstance(Moves, Depth, Length + Mag);
depthstance([[<<"down">>, Mag] | Moves], Depth, Length) ->
    depthstance(Moves, Depth + Mag, Length);
depthstance([[<<"up">>, Mag] | Moves], Depth, Length) ->
    depthstance(Moves, Depth - Mag, Length).

intify_move([Dir, Mag]) ->
    {Magn, _} = string:to_integer(Mag),
    [Dir, Magn].

solve(List) ->
    Pairs = lists:map(fun (S) -> string:split(S, " ") end, List),
    depthstance(lists:map(fun intify_move/1, Pairs), 0, 0).

doproblem() ->
    {ok, Text} = file:read_file("input.txt"),
    solve(string:split(Text, "\n", all)).
