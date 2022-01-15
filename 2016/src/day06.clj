(require '[clojure.string :as string])

(defn correct-errors [messages sort-key]
  (->> (apply map vector messages)
       (map #(key (first (sort sort-key (frequencies %)))))
       (apply str)))

(defn part1 [input]
  (correct-errors (string/split-lines input) #(> (val %1) (val %2))))

(defn part2 [input]
  (correct-errors (string/split-lines input) #(< (val %1) (val %2))))

(def sample (slurp "../samples/day06.txt"))
(assert (= (part1 sample) "easter"))
(assert (= (part2 sample) "advent"))

(def input (slurp "../inputs/day06.txt"))
(println {:silver (part1 input) :gold (part2 input)})
