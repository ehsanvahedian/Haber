"use client";

import { useRef, useState } from "react";
import {
  motion,
  useScroll,
  useTransform,
  useMotionValueEvent,
} from "framer-motion";
import {
  ArrowDownLeft,
  ArrowUpRight,
  ArrowBigUpIcon,
  Check,
  CreditCard,
  Wallet,
} from "lucide-react";

import { universeItems } from "./universe-data";
import type { UniverseItem } from "./types";

// تابع محاسبه دقیق موقعیت نهایی آیتم‌ها روی کارت‌ها (به درصد از کل ویوپورت)
const getTargetPosition = (id: string) => {
  // فاز اول: آرتیکل‌ها (متن منظم و تراز شده در مرکز کارت اول بدون فاصله زیاد)
  if (id === "quote-1") return { x: 50, y: 34 };
  if (id === "quote-2") return { x: 50, y: 39 };
  if (id === "quote-3") return { x: 50, y: 44 };
  if (id === "quote-4") return { x: 50, y: 49 };
  if (id === "quote-5") return { x: 50, y: 54 };
  if (id === "quote-6") return { x: 50, y: 59 };
  if (id === "quote-7") return { x: 50, y: 64 };
  if (id === "quote-8") return { x: 50, y: 69 };
  if (id === "quote-9") return { x: 50, y: 74 };
  if (id === "quote-10") return { x: 50, y: 79 };

  // فاز دوم: تسک‌ها (مرتب شده در ۲ ستون منظم بدون تداخل با روتیشن صفر)
  if (id === "task-1") return { x: 40, y: 36 };
  if (id === "task-2") return { x: 60, y: 36 };
  if (id === "task-3") return { x: 40, y: 45 };
  if (id === "task-4") return { x: 60, y: 45 };
  if (id === "task-5") return { x: 40, y: 54 };
  if (id === "task-6") return { x: 60, y: 54 };
  if (id === "task-7") return { x: 40, y: 63 };
  if (id === "task-8") return { x: 60, y: 63 };
  if (id === "task-9") return { x: 40, y: 72 };
  if (id === "task-10") return { x: 60, y: 72 };

  // فاز سوم: ترکیب سه تایی درآمد، بدهی و تراکنش‌ها در ۳ ستون مجزا
  const rowSpacing = [36, 40, 44, 48, 52, 56, 60, 64, 68, 72];
  if (id.startsWith("income-")) {
    const idx = parseInt(id.split("-")[1]) - 1;
    return { x: 38, y: rowSpacing[idx] || 36 };
  }
  if (id.startsWith("debt-")) {
    const idx = parseInt(id.split("-")[1]) - 1;
    return { x: 50, y: rowSpacing[idx] || 36 };
  }
  if (id.startsWith("transaction-")) {
    const idx = parseInt(id.split("-")[1]) - 1;
    return { x: 62, y: rowSpacing[idx] || 36 };
  }

  return null;
};

function UniverseItemContent({ item }: { item: UniverseItem }) {
  switch (item.type) {
    case "word":
      return (
        <span className="text-sm font-medium tracking-tight text-neutral-400">
          {item.content}
        </span>
      );
    case "number":
      return (
        <span className="text-base font-medium tracking-tight text-neutral-500">
          {item.content}
        </span>
      );
    case "income":
      return (
        <div className="flex items-center gap-2 text-sm font-medium text-emerald-500">
          <ArrowUpRight size={14} strokeWidth={2} />
          <span>{item.content.replace(" income", "")}</span>
        </div>
      );
    case "debt":
      return (
        <div className="flex items-center gap-2 text-sm font-medium text-rose-400">
          <ArrowDownLeft size={14} strokeWidth={2} />
          <span>{item.content.replace(" debt", "")}</span>
        </div>
      );
    case "task":
      return (
        <div className="flex items-center gap-2 text-sm text-neutral-200">
          <span className="flex h-4 w-4 items-center justify-center rounded-full border border-neutral-500 bg-neutral-800">
            <Check size={9} className="text-neutral-300" />
          </span>
          <span>{item.content}</span>
        </div>
      );
    case "transaction":
      return (
        <div className="flex items-center gap-2 text-sm text-neutral-400">
          <CreditCard size={14} strokeWidth={1.6} />
          <span>{item.content}</span>
        </div>
      );
    case "icon":
      return <Wallet size={16} />;
    default:
      return null;
  }
}

function UniversalFlyingItem({
  item,
  scrollYProgress,
}: {
  item: UniverseItem;
  scrollYProgress: any;
}) {
  const isQuote = item.id.startsWith("quote-");
  const isTask = item.id.startsWith("task-");
  const isIncome = item.id.startsWith("income-");
  const isDebt = item.id.startsWith("debt-");
  const isTransaction = item.id.startsWith("transaction-");
  const isExtra = !isQuote && !isTask && !isIncome && !isDebt && !isTransaction;

  const target = getTargetPosition(item.id);
  const [shouldFreeze, setShouldFreeze] = useState(false);
  // مانیتور کردن اسکرول برای صاف کردن استایل لرزش در زمان مناسب
  useMotionValueEvent(scrollYProgress, "change", (latest: number) => {
    if (isQuote && latest > 0.1) setShouldFreeze(true);
    else if (isTask && latest > 0.35) setShouldFreeze(true);
    else if ((isIncome || isDebt || isTransaction) && latest > 0.7) setShouldFreeze(true);
    else if (latest < 0.05) setShouldFreeze(false);
  });

  // تعریف مقادیر انیمیشن منطبق بر تایم‌لاین درخواستی شما
  let timeline = [0, 1];
  let xValues = [item.x, item.x];
  let yValues = [item.y, item.y];
  let rValues = [item.rotation, item.rotation];
  let opacityValues = [0, 1]; // ظاهر شدن از 0 تا 10٪ مابقی پایین ست می‌شود

  if (isQuote && target) {
    timeline = [0, 0.1, 0.3, 0.35, 1.0];
    xValues = [item.x, item.x, target.x, target.x, target.x];
    yValues = [item.y, item.y, target.y, target.y, target.y];
    rValues = [item.rotation, item.rotation, 0, 0, 0];
    opacityValues = [1, 1, 1, 0, 0];
  } else if (isTask && target) {
    timeline = [0, 0.35, 0.65, 0.7, 1.0];
    xValues = [item.x, item.x, target.x, target.x, target.x];
    yValues = [item.y, item.y, target.y, target.y, target.y];
    rValues = [item.rotation, item.rotation, 0, 0, 0];
    opacityValues = [1, 1, 1, 0, 0];
  } else if ((isIncome || isDebt || isTransaction) && target) {
    timeline = [0, 0.7, 0.95, 1.0];
    xValues = [item.x, item.x, target.x, target.x];
    yValues = [item.y, item.y, target.y, target.y];
    rValues = [item.rotation, item.rotation, 0, 0];
    opacityValues = [1, 1, 1, 0];
  } else if (isExtra) {
    // ۲۰ مورد اضافی همزمان با حرکت ترانزکشن‌ها (از ۷۰ تا ۹۵٪) محو می‌شوند
    timeline = [0, 0.7, 0.95, 1.0];
    xValues = [item.x, item.x, item.x, item.x];
    yValues = [item.y, item.y, item.y, item.y];
    rValues = [item.rotation, item.rotation, item.rotation, item.rotation];
    opacityValues = [1, 1, 0, 0];
  }

  // اضافه کردن حالت انیمیشن ورودی (0 تا 10٪ ظاهر شدن کلیه آیتم‌ها)
  const baseOpacity = useTransform(scrollYProgress, [0, 0.1], [0, 1]);
  const transformOpacity = useTransform(scrollYProgress, timeline, opacityValues);
  const finalOpacity = useTransform(() => 
    scrollYProgress.get() <= 0.1 ? baseOpacity.get() : transformOpacity.get()
  );

  const rawX = useTransform(scrollYProgress, timeline, xValues);
  const rawY = useTransform(scrollYProgress, timeline, yValues);
  const left = useTransform(rawX, (v) => `${v}%`);
  const top = useTransform(rawY, (v) => `${v}%`);
  const rotate = useTransform(scrollYProgress, timeline, rValues);

  return (
    <motion.div
      className="absolute -translate-x-1/2 -translate-y-1/2 whitespace-nowrap z-20 select-none"
      style={{ left, top, rotate, opacity: finalOpacity }}
    >
      <motion.div
        animate={shouldFreeze ? { x: 0, y: 0 } : {
          x: [0, 1.8, -1.8, 0],
          y: [0, -2, 2, 0],
        }}
        transition={shouldFreeze ? { duration: 0.2 } : {
          duration: item.duration || 4,
          repeat: Infinity,
          ease: "easeInOut",
          delay: item.delay || 0,
        }}
      >
        <UniverseItemContent item={item} />
      </motion.div>
    </motion.div>
  );
}

export default function FinancialUniverse() {
  const universeRef = useRef<HTMLElement | null>(null);

  const { scrollYProgress } = useScroll({
    target: universeRef,
    offset: ["start start", "end end"],
  });

  // کنترلر ترنزیشن‌های کارت اول (10% تا 30% ورود، 30% تا 35% خروج)
  const card1Opacity = useTransform(scrollYProgress, [0.1, 0.11, 0.34, 0.35], [0, 1, 1, 0]);
  const card1Y = useTransform(scrollYProgress, [0.1, 0.15, 0.3, 0.39], [40, 0, 0, -40]);

  // کنترلر ترنزیشن‌های کارت دوم (35% تا 65% ورود، 65% تا 70% خروج)
  const card2Opacity = useTransform(scrollYProgress, [0.35, 0.36, 0.69, 0.70], [0, 1, 1, 0]);
  const card2Y = useTransform(scrollYProgress, [0.35, 0.4, 0.65, 0.75], [40, 0, 0, -40]);

  // کنترلر ترنزیشن‌های کارت سوم (70% تا 95% ورود، 95% تا 100% خروج)
  const card3Opacity = useTransform(scrollYProgress, [0.7, 0.71, 0.99, 1.0], [0, 1, 1, 0]);
  const card3Y = useTransform(scrollYProgress, [0.7, 0.75, 0.95, 1.0], [40, 0, 0, -40]);

  // نمایش تگ نهایی اچ‌دو (95% تا 100%)
  const finalMessageOpacity = useTransform(scrollYProgress, [0.97, 0.98], [0, 1]);
  const finalScale = useTransform(scrollYProgress, [0.95, 1.0], [0.95, 1]);

  return (
    <section ref={universeRef} className="relative h-[450vh] w-full bg-grad">
      <div className="pt-50 flex justify-center">
        <ArrowBigUpIcon className="m-auto"/>
        <p>scroll</p>
        <ArrowBigUpIcon className="m-auto"/>
        <p>scroll</p>
        <ArrowBigUpIcon className="m-auto"/>
        <p>scroll</p>
        <ArrowBigUpIcon className="m-auto"/>
      </div>
      <div className="sticky top-0 h-screen w-full overflow-hidden  pt-50">
        
        {/* رندر تمام آیتم‌های جهان اتمی به صورت یکپارچه در لایه پس‌زمینه */}
        <div className="absolute inset-0 w-full h-full pointer-events-none">
          {universeItems.map((item) => (
            <UniversalFlyingItem
              key={item.id}
              item={item}
              scrollYProgress={scrollYProgress}
            />
          ))}
        </div>

        {/* کارت اول: Organized Mind */}
        <motion.article
          style={{ opacity: card1Opacity, y: card1Y }}
          className="absolute left-1/2 top-1/2 z-10 w-[640px] h-[520px] -translate-x-1/2 -translate-y-1/2 rounded-[32px] border border-white/[0.1] bg-neutral-900/80 backdrop-blur-2xl p-10 flex flex-col items-center"
        >
          <h2 className="text-3xl font-medium tracking-tight text-neutral-200 text-center">
            Organized Mind
          </h2>
          {/* محفظه خالی برای فرود منظم متن‌های آرتیکل */}
          <div className="w-full flex-1 mt-6" />
        </motion.article>

        {/* کارت دوم: Tasks & Todos */}
        <motion.article
          style={{ opacity: card2Opacity, y: card2Y }}
          className="absolute left-1/2 top-1/2 z-10 w-[640px] h-[520px] -translate-x-1/2 -translate-y-1/2 rounded-[32px] border border-white/[0.06] bg-neutral-900/80 backdrop-blur-2xl p-10 flex flex-col"
        >
          <h2 className="text-3xl font-medium tracking-tight text-neutral-200 text-center mb-6">
            Tasks & Todos
          </h2>
          <div className="w-full flex-1" />
        </motion.article>

        {/* کارت سوم: Expenses, Incomes, Debts */}
        <motion.article
          style={{ opacity: card3Opacity, y: card3Y }}
          className="absolute left-1/2 top-1/2 z-10 w-[680px] h-[520px] -translate-x-1/2 -translate-y-1/2 rounded-[32px] border border-white/[0.06] bg-neutral-900/80 backdrop-blur-2xl p-10 flex flex-col"
        >
          <div className="grid grid-cols-3 gap-4 text-center border-b border-white/5 pb-4">
            <h3 className="text-sm font-semibold text-emerald-500 tracking-wide uppercase">Incomes</h3>
            <h3 className="text-sm font-semibold text-rose-400 tracking-wide uppercase">Debts</h3>
            <h3 className="text-sm font-semibold text-neutral-400 tracking-wide uppercase">Transactions</h3>
          </div>
          <div className="w-full flex-1" />
        </motion.article>

        {/* پیام نهایی اختصاصی Haber در پایان اسکرول */}
        <motion.div
          className="absolute inset-0 flex items-center justify-center z-30 px-6"
          style={{ opacity: finalMessageOpacity, scale: finalScale }}
        >
          <h2 className="text-4xl md:text-5xl font-medium tracking-tight text-neutral-100 text-center max-w-2xl leading-snug">
            You can have a organized Mind and life with Haber !
          </h2>
        </motion.div>

      </div>
    </section>
  );
}