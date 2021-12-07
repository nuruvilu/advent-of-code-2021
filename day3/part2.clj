
(require '[clojure.string :as string])

(defn get-x-reading [nums so-far i sort-key]
    (if (= (count nums) 1)
      (Integer/parseInt (nth nums 0) 2)
      (let [column (apply str (map #(nth % i) nums))
            ones (count (filter #(= % \1) column))
            zeros (- (count column) ones)
            new-so-far (str so-far (if (sort-key ones zeros) "1" "0"))]
        (get-x-reading
         (filter #(string/starts-with? % new-so-far) nums)
         new-so-far
         (inc i)
         sort-key))))

(defn solve [input-list]
  (* (get-x-reading input-list "" 0 >=) (get-x-reading input-list "" 0 <)))

(println (solve (string/split-lines (slurp "input.txt"))))
