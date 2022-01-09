(require '[clojure.string :as string])

(defn turn [dir turn-str]
  (mod (+ dir (if (= turn-str \R) 1 -1)) 4))

(defn step [steps dir pos]
  (map + pos (nth [[steps 0] [0 steps] [(- steps) 0] [0 (- steps)]] dir)))

(defn man-dist [p1 p2]
  (->> (map - p2 p1)
       (map #(Math/abs %))
       (reduce +)))

(defn walk [directions dir pos]
  (if (empty? directions)
    pos
    (let [[move & moves] directions
          [turn-str & length-str] move
          new-dir (turn dir turn-str)]
      (recur moves new-dir
             (step (Integer/parseInt (string/join length-str)) new-dir pos)))))

(defn interms [[x1 y1] [x2 y2]]
  (if (= x1 x2)
    (let [pol (if (< y2 y1) -1 1)]
      (map vector (repeat x1) (range (+ y1 pol) (+ y2 pol) pol)))
    (let [pol (if (< x2 x1) -1 1)]
      (map vector (range (+ x1 pol) (+ x2 pol) pol) (repeat y1)))))

(defn find-hq [directions dir pos visited]
  (let [[move & moves] directions
        [turn-str & length-str] move
         new-dir (turn dir turn-str)
         new-pos (step (Integer/parseInt (string/join length-str)) new-dir pos)
         interms (interms pos new-pos)
         already-visited (filter #(contains? visited %) interms)]
    (if (empty? already-visited)
      (recur moves new-dir new-pos (apply conj visited interms))
      (first already-visited))))

(defn parse [text] (string/split text #", "))

(defn part1 [text] (man-dist [0 0] (walk (parse text) 0 [0 0])))

(defn part2 [text] (man-dist [0 0] (find-hq (parse text) 0 [0 0] #{[0 0]})))

(assert (= (part1 "R2, L3") 5))
(assert (= (part1 "R2, R2, R2") 2))
(assert (= (part1 "R5, L5, R5, R3") 12))
(assert (= (part2 "R8, R4, R4, R8") 4))

(def input (slurp "../inputs/day1.txt"))
(println {:silver (part1 input) :gold (part2 input)})
