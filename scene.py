from manim import *


class Main(Scene):
    def construct(self):
        # Set theory chapter

        # Set A
        circleA = Circle(color=WHITE, fill_opacity=0.0, stroke_width=2)
        self.play(Create(circleA), run_time=3)
        self.wait(1)

        # Title
        tex = Tex("Sets", color=WHITE, font_size=72).move_to(DOWN * 2)
        self.play(Write(tex))
        self.wait(1)

        # Set Name
        texA = Tex("A", color=WHITE, font_size=48)
        self.play(FadeIn(texA))

        # Set B
        circleB = Circle(color=WHITE, fill_opacity=0.0, stroke_width=2).shift(RIGHT * 0.7)
        texB = Tex("B", color=WHITE, font_size=48).shift(RIGHT * 0.7)
        self.play(
            Create(circleB),
            circleA.animate.shift(LEFT*0.7),
            texA.animate.shift(LEFT*0.7),
            FadeIn(texB),
            Unwrite(tex),
            run_time=2
        )
        self.wait(1)

        # Add elements to the set and show the sets in text below

        # Roster Form
        texSetA = MathTex(r"Roster \: Form: \: A = \{  1, 2, 3, 4  \}", color=WHITE, font_size=48, opacity=1)\
            .shift(DOWN * 2)

        # Set Builder Notation
        texSetB = MathTex(r"Set \: Builder \: Form: \: B = \{  x : x \, \epsilon \, N, \, 3< x < 8  \}", color=WHITE,
                          font_size=48, opacity=1).shift(DOWN * 3)

        texElement1 = MathTex(r"1", color=WHITE, font_size=32, opacity=0.5).shift(LEFT * 0.7, UP * 0.7)
        texElement2 = MathTex(r"2", color=WHITE, font_size=32, opacity=0.5).shift(LEFT * 1.4)
        texElement3 = MathTex(r"3", color=WHITE, font_size=32, opacity=0.5).shift(LEFT * 0.7, DOWN * 0.7)
        texElement4 = MathTex(r"4", color=WHITE, font_size=32, opacity=0.5)
        texElement5 = MathTex(r"5", color=WHITE, font_size=32, opacity=0.5).shift(RIGHT * 0.7, UP * 0.7)
        texElement6 = MathTex(r"6", color=WHITE, font_size=32, opacity=0.5).shift(RIGHT * 1.4)
        texElement7 = MathTex(r"7", color=WHITE, font_size=32, opacity=0.5).shift(RIGHT * 0.7, DOWN * 0.7)
        self.play(
            FadeIn(texSetA),
            FadeIn(texSetB),
            FadeIn(texElement1),
            FadeIn(texElement2),
            FadeIn(texElement3),
            FadeIn(texElement4),
            FadeIn(texElement5),
            FadeIn(texElement6),
            FadeIn(texElement7),
            run_time=2
        )
        self.wait(2)

        self.play(
            FadeOut(texSetA),
            FadeOut(texSetB),
            FadeOut(texElement1),
            FadeOut(texElement2),
            FadeOut(texElement3),
            FadeOut(texElement4),
            FadeOut(texElement5),
            FadeOut(texElement6),
            FadeOut(texElement7),
            run_time=2
        )

        self.wait(1)

        # Types of sets
        self.add(circleA, circleB)
        vt = ValueTracker(10)

        def update_circle_opacity(circle):
            alpha = vt.get_value() / 10
            circle.set_stroke(opacity=alpha)

        self.play(
            UpdateFromFunc(circleA, update_circle_opacity),
            UpdateFromFunc(circleB, update_circle_opacity),
            circleA.animate.shift(RIGHT * 0.7),
            circleB.animate.shift(LEFT * 0.7),
            texA.animate.shift(RIGHT * 0.7),
            vt.animate.set_value(5),
            FadeOut(texA),
            texB.animate.shift(LEFT * 0.7),
            FadeOut(texB),
            run_time=2,
            rate_func=linear,
        )
        self.wait(1)

        circleA.set_stroke(opacity=1)
        circleB.set_stroke(opacity=1)
        circleC = Circle(color=WHITE, fill_opacity=0.0, stroke_width=2)
        circleD = Circle(color=WHITE, fill_opacity=0.0, stroke_width=2)
        circleE = Circle(color=WHITE, fill_opacity=0.0, stroke_width=2)
        circleF = Circle(color=WHITE, fill_opacity=0.0, stroke_width=2)
        circleG = Circle(color=WHITE, fill_opacity=0.0, stroke_width=2)
        circleH = Circle(color=WHITE, fill_opacity=0.0, stroke_width=2)

        self.play(
            circleC.animate.shift(RIGHT * 5),
            circleD.animate.shift(LEFT * 5),
            circleA.animate.shift(LEFT * 2),
            circleB.animate.shift(RIGHT * 2),
            circleE.animate.shift(RIGHT * 1.3, DOWN * 2.3),
            circleF.animate.shift(LEFT * 1.3, DOWN * 2.3),
            circleG.animate.shift(RIGHT * 1.3, UP * 2.3),
            circleH.animate.shift(LEFT * 1.3, UP * 2.3),
            run_time=2
        )
        self.wait(1)

        texSingleton = Tex(r"Singleton \\ Set", color=WHITE, font_size=32).shift(LEFT * 2)
        texSingletonEle = Tex("Paris", color=WHITE, opacity=0.5, font_size=16).shift(UP * 0.6, LEFT * 2)
        texEmpty = Tex(r"Empty \\ Set", color=WHITE, font_size=32).shift(RIGHT * 2)
        texFinite = Tex(r"Finite \\ Set", color=WHITE, font_size=32).shift(LEFT * 5, UP * 0.3)
        texFiniteEle = MathTex(r"\{  1, 2, 3, 4  \}", color=WHITE, opacity=0.5, font_size=16)\
            .shift(LEFT * 5, DOWN * 0.5)
        texInfinite = Tex(r"Infinite \\ Set", color=WHITE, font_size=32).shift(RIGHT * 5, UP * 0.3)
        texInfiniteEle = MathTex(r"\{  1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...  \}", color=WHITE, opacity=0.5, font_size=16)\
            .shift(RIGHT * 5, DOWN * 0.5)
        texEqual = Tex("Equal Sets", color=WHITE, font_size=32).shift(UP * 1)
        texEqualEle = MathTex(r"\{  1, 2, 3, 4  \}", color=WHITE, opacity=0.5, font_size=16)\
            .shift(UP * 2.3, LEFT * 1.3)
        texEqualEle2 = MathTex(r"\{  4, 3, 2, 1  \}", color=WHITE, opacity=0.5, font_size=16)\
            .shift(UP * 2.3, RIGHT * 1.3)
        texEquivalent = Tex("Equivalent Sets", color=WHITE, font_size=32).shift(DOWN * 3.6)
        texEquivalentEle = MathTex(r"\{  A, B, C, D  \}", color=WHITE, opacity=0.5, font_size=16)\
            .shift(DOWN * 2.3, RIGHT * 1.3)
        texEquivalentEle2 = MathTex(r"\{  Tim, \, Blake, \\ Candice, \\ Ben  \}", color=WHITE, opacity=0.5,
                                    font_size=16).shift(DOWN * 2.3, LEFT * 1.3)

        self.play(
            Write(texSingleton),
            FadeIn(texSingletonEle),
            Write(texEmpty),
            Write(texFinite),
            FadeIn(texFiniteEle),
            Write(texInfinite),
            FadeIn(texInfiniteEle),
            Write(texEqual),
            FadeIn(texEqualEle),
            FadeIn(texEqualEle2),
            Write(texEquivalent),
            FadeIn(texEquivalentEle),
            FadeIn(texEquivalentEle2),
            run_time=2
        )

        self.wait(5)

        self.play(
            Unwrite(texSingleton),
            FadeOut(texSingletonEle),
            Unwrite(texEmpty),
            Unwrite(texFinite),
            FadeOut(texFiniteEle),
            Unwrite(texInfinite),
            FadeOut(texInfiniteEle),
            Unwrite(texEqual),
            FadeOut(texEqualEle),
            FadeOut(texEqualEle2),
            Unwrite(texEquivalent),
            FadeOut(texEquivalentEle),
            FadeOut(texEquivalentEle2),
            run_time=2
        )

        self.wait(2)

        circleI = Circle(color=WHITE, fill_opacity=0.0, stroke_width=2).shift(RIGHT * 2)
        box = Rectangle(color=WHITE, fill_opacity=0.0, stroke_width=2, height=3, width=4).shift(LEFT * 5)

        self.play(
            circleI.animate.shift(RIGHT * 1.6),
            circleC.animate.shift(LEFT * 0),
            Create(box),
            circleA.animate.shift(RIGHT * 1.5),
            circleB.animate.shift(LEFT * 1.5),
            circleE.animate.shift(LEFT * 0.8),
            circleF.animate.shift(RIGHT * 0.8),
            circleG.animate.shift(LEFT * 0.8),
            circleH.animate.shift(RIGHT * 0.8),
            run_time=2
        )

        self.wait(1)

        uni = Union(circleA, circleB, color="#428ea1", fill_opacity=1, stroke_width=0)
        texUni = MathTex(r"Union \\ A \, \cup \, B", color=WHITE, font_size=32)
        ex = Exclusion(circleG, circleH, color="#428ea1", fill_opacity=1, stroke_width=0)
        texEx = MathTex(r"Symmetric \\ Difference", color=WHITE, font_size=32).shift(UP * 2.6)
        texEx_1 = MathTex(r"A \, \triangle \, B", color=WHITE, font_size=32).shift(UP * 1.8)
        inter = Intersection(circleE, circleF, color="#428ea1", fill_opacity=1, stroke_width=0)
        texInter = MathTex(r"Intersection", color=WHITE, font_size=32).shift(DOWN * 1.9)
        texInter_1 = MathTex(r"A \, \cap \, B", color=WHITE, font_size=32).shift(DOWN * 2.5)
        diff1 = Difference(box, circleD, color="#428ea1", fill_opacity=1, stroke_width=0)
        texDiff1 = MathTex(r"Complement", color=WHITE, font_size=32).shift(LEFT * 5, UP * 0.5)
        texDiff1_2 = MathTex(r"B^\complement", color=WHITE, font_size=32).shift(LEFT * 5)
        texDiff1_3 = MathTex(r"U \, - \, B", color=WHITE, font_size=32).shift(LEFT * 5, DOWN * 0.5)
        diff2 = Difference(circleC, circleI, color="#428ea1", fill_opacity=1, stroke_width=0)
        texDiff2 = MathTex(r"Difference", color=WHITE, font_size=32).shift(RIGHT * 4.3, UP * 0.25)
        texDiff2_1 = MathTex(r"B \, - \, A", color=WHITE, font_size=32).shift(RIGHT * 4.3, DOWN * 0.25)

        self.play(
            FadeIn(uni),
            FadeIn(ex),
            FadeIn(inter),
            FadeIn(diff1),
            FadeIn(diff2),
            Write(texUni),
            Write(texEx),
            Write(texEx_1),
            Write(texInter),
            Write(texInter_1),
            Write(texDiff1),
            Write(texDiff1_2),
            Write(texDiff1_3),
            Write(texDiff2),
            Write(texDiff2_1),
            run_time=2
        )

        self.wait(4)

        self.play(
            FadeOut(uni),
            FadeOut(ex),
            FadeOut(inter),
            FadeOut(diff1),
            FadeOut(diff2),
            FadeOut(texUni),
            FadeOut(texEx),
            FadeOut(texEx_1),
            FadeOut(texInter),
            FadeOut(texInter_1),
            FadeOut(texDiff1),
            FadeOut(texDiff1_2),
            FadeOut(texDiff1_3),
            FadeOut(texDiff2),
            FadeOut(texDiff2_1),
            Uncreate(box),
            run_time=2
        )

        self.wait(1)

        self.play(
            circleB.animate.shift(LEFT * 0.5),
            circleC.animate.shift(LEFT * 5),
            circleD.animate.shift(RIGHT * 5),
            circleE.animate.shift(LEFT * 0.5, UP * 2.3),
            circleF.animate.shift(RIGHT * 0.5, UP * 2.3),
            circleG.animate.shift(LEFT * 0.5, DOWN * 2.3),
            circleH.animate.shift(RIGHT * 0.5, DOWN * 2.3),
            circleI.animate.shift(LEFT * 3.6),
            circleA.animate.shift(RIGHT * 0.5),
            run_time=2,
            rate_func=linear,
        )

        self.play(
            Uncreate(circleB),
            Uncreate(circleC),
            Uncreate(circleD),
            Uncreate(circleE),
            Uncreate(circleF),
            Uncreate(circleG),
            Uncreate(circleH),
            Uncreate(circleI),
            Uncreate(circleA),
            run_time=1,
            rate_func=linear,
        )
        self.wait(1)
