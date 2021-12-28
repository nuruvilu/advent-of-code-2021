
(require '[clojure.string :as string])

(defn do-row [row num]
  (if (some #(= num %) row) (replace {num -1} row) row))

(defn check-row [row]
  (= (reduce + row) -5))

(defn check-board [board]
  (or
   (reduce #(or %1 %2) (map check-row board))
   (reduce #(or %1 %2) (map check-row (apply map vector board)))))

(defn parse-board [board-string]
  (->> board-string
       (string/split-lines)
       (map #(map (fn [s] (Integer/parseInt s))
                  (filter (fn [s] (not= s "")) (string/split % #" "))))))

(defn get-score [board num]
  (* num
     (->> board
          (map #(filter (fn [n] (not= n -1)) %))
          (map #(reduce + %))
          (reduce +))))

(defn step [nums board steps]
  (let [new-board (map #(do-row % (first nums)) board)]
    (if (check-board new-board)
      [steps (get-score new-board (first nums))]
      (step (rest nums) new-board (inc steps)))))

(defn solve [input-list]
  (let [nums (map #(Integer/parseInt %)
                  (filter #(not= % "")
                          (string/split (first input-list) #",")))]
    (->> (map parse-board (rest input-list))
         (map #(step nums % 0))
         (sort-by first)
         (#(identity [:silver (first %) :gold (last %)])))))

(println (solve (string/split (slurp "input.txt") #"\n\n")))
