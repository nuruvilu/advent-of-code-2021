-module(part1).
-export([doproblem/0]).

incr_tallies(49, {{1, O}, {0, Z}}) ->
    {{1, O + 1}, {0, Z}};
incr_tallies(48, {{1, O}, {0, Z}}) ->
    {{1, O}, {0, Z + 1}}.

incr_gam_eps({1, O}, {0, Z}, Gamma, Epsilon) when O > Z ->
    {Gamma bsl 1 + 1, Epsilon bsl 1};
incr_gam_eps({1, O}, {0, Z}, Gamma, Epsilon) when O =< Z ->
    {Gamma bsl 1, Epsilon bsl 1 + 1}.

get_gam_eps(_, I, Gamma, Epsilon, NumLength) when I > NumLength ->
    {Gamma, Epsilon};
get_gam_eps(Nums, I, Gamma, Epsilon, NumLength) ->
    Column = [lists:nth(I, bitstring_to_list(Num)) || Num <- Nums],
    {Ones, Zeroes} = lists:foldl(fun incr_tallies/2, {{1, 0}, {0, 0}}, Column),
    {GP, EP} = incr_gam_eps(Ones, Zeroes, Gamma, Epsilon),
    get_gam_eps(Nums, I + 1, GP, EP, NumLength).

solve(List) ->
    [FirstNum | _] = List,
    NumLength = string:length(FirstNum),
    {Gamma, Epsilon} = get_gam_eps(List, 1, 0, 0, NumLength),
    Gamma * Epsilon.

doproblem() ->
    {ok, Text} = file:read_file("input.txt"),
    solve(string:split(Text, "\n", all)).
