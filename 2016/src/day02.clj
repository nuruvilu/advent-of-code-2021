(require '[clojure.string :as string])

(def keypad1 (map str (range 1 10)))

(def keypad2 [\. \. \1 \. \.
              \. \2 \3 \4 \.
              \5 \6 \7 \8 \9
              \. \A \B \C \.
              \. \. \D \. \.])

(defn move-by [pos instruction dim reset?]
  (let [new-pos 
        (cond
          (and (= instruction \U) (>= pos dim)) (- pos dim)
          (and (= instruction \L) (not= (mod pos dim) 0)) (dec pos)
          (and (= instruction \D) (< pos (* dim (dec dim)))) (+ pos dim)
          (and (= instruction \R) (not= (mod pos dim) (dec dim))) (inc pos)
          :else pos)]
    (if (reset? new-pos) pos new-pos)))

(defn enter-code [instructions pos code move keypad]
  (if (empty? instructions)
    code
    (let [new-pos (reduce move pos (first instructions))]
      (recur (rest instructions)
             new-pos
             (str code (nth keypad new-pos))
             move keypad))))

(defn part1 [input]
  (enter-code (string/split-lines input) 4 ""
              #(move-by %1 %2 3 (constantly false)) keypad1))

(defn part2 [input]
  (enter-code (string/split-lines input) 10 ""
              #(move-by %1 %2 5 (fn [p] (= (keypad2 p) \.))) keypad2))

(def sample (slurp "../samples/day02.txt"))
(assert (= (part1 sample) "1985"))
(assert (= (part2 sample) "5DB3"))

(def input (slurp "../inputs/day02.txt"))
(println {:silver (part1 input) :gold (part2 input)})
