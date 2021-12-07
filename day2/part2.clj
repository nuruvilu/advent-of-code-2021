
(require '[clojure.string :as string])

(defn depthstance [moves aim depth length]
  (if (empty? moves)
    (* depth length)
    (let [dir ((first moves) 0)
          mag (Integer/parseInt ((first moves) 1))]
      (if (= dir "forward")
        (depthstance (rest moves) aim (+ depth (* aim mag)) (+ length mag))
        (depthstance (rest moves) (+ aim (* mag (if (= dir "down") 1 -1))) depth length)))))

(defn solve [input-list]
  (depthstance (map #(string/split % #" ") input-list) 0 0 0))

(println (solve (string/split-lines (slurp "input.txt"))))
