-module(part1).
-export([doproblem/0]).

%%%% THIS DOESNT WORK BTW :^)

to_int(S) ->
    {N, _} = string:to_integer(S),
    N.

filter_error(error) -> false;
filter_error(_) -> true.

parse_row(RowString) ->
    Row = lists:map(fun to_int/1, string:split(RowString, " ", all)),
    lists:filter(fun filter_error/1, Row).

parse_board(BoardString) ->
    RowStrings = string:split(BoardString, "\n", all),
    lists:map(fun parse_row/1, RowStrings).

build_nums_map([Num], NumsMap, I) ->
    maps:put(Num, I, NumsMap);
build_nums_map([Num | Nums], NumsMap, I) ->
    build_nums_map(Nums, maps:put(Num, I, NumsMap), I + 1).

build_win_row(Row, NumsMap) ->
    WinMap = lists:map(fun (N) -> maps:get(N, NumsMap) end, Row),
    lists:map(fun ({ok, Win}) -> Win end, WinMap).

build_win_board(Board, NumsMap) ->
    lists:map(fun (R) -> build_win_row(R, NumsMap) end, Board).

pivot_board(Board, 1, Acc) ->
    [lists:map(fun (R) -> lists:nth(1, R) end, Board) | Acc];
pivot_board(Board, I, Acc) ->
    pivot_board(
        Board,
        I + 1,
        [lists:map(fun (R) -> lists:nth(I, R) end, Board) | Acc]
    ).

get_win_turn(WinBoard) ->
    lists:min(lists:merge(
        lists:map(fun lists:max/1, WinBoard),
        lists:map(fun lists:max/1, pivot_board(WinBoard, 5, []))
    )).

wind([WinRow], [Row], Acc) ->
    [lists:zip(WinRow, Row) | Acc];
wind([WinRow | WinRows], [Row | Rows], Acc) ->
    wind(WinRows, Rows, [lists:zip(WinRow, Row) | Acc]).

unwind_score({T, _}, WinTurn) when T > WinTurn -> 0;
unwind_score({T, N}, WinTurn) when T =< WinTurn -> N.

get_score(Board, WinBoard, WinTurn) ->
    WoundBoards = wind(WinBoard, Board, []),
    Flattened = lists:flatten(WoundBoards),
    lists:sum(lists:map(fun (X) -> unwind_score(X, WinTurn) end, Flattened)).

solve_board(Board, NumsMap, Nums) ->
    WinBoard = build_win_board(Board, NumsMap),
    WinTurn = get_win_turn(WinBoard),
    lists:nth(WinTurn, Nums) * get_score(Board, WinBoard, WinTurn).

solve([NumString | BoardStrings]) ->
    Nums = lists:map(
        fun to_int/1,
        string:split(NumString, ",", all)
    ),
    NumsMap = build_nums_map(Nums, maps:new(), 1),
    Boards = lists:map(fun parse_board/1, BoardStrings),
    SolvedBoards = lists:map(
        fun (B) -> solve_board(B, NumsMap, Nums) end,
        Boards
    ),
    [First | _] = lists:sort(fun ({A, _}, {B, _}) -> A =< B end, SolvedBoards),
    First.

doproblem() ->
    {ok, Text} = file:read_file("input.txt"),
    solve(string:split(Text, "\n\n", all)).
